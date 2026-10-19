import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("dark_background")

COR_PRINCIPAL = "#2ECC71"
COR_SECUNDARIA = "#1B4332"
COR_TEXTO = "#F5F5F5"
COR_FUNDO = "#121826"

print("Football Data Insights")

jogadores = pd.read_csv("player_stats.csv")
print(jogadores.head())

print(jogadores.columns.tolist())
print(jogadores.shape)
print(len(jogadores))

paises = jogadores["country"].value_counts()

print("\n5 países com mais jogadores:")
print(paises.head(5))

top_cinco = paises.head(5)

plt.figure(figsize=(10, 6))

ax = top_cinco.plot(
    kind="bar",
    color=COR_PRINCIPAL,
    edgecolor=COR_SECUNDARIA,
    width=0.7
)

plt.title(
    "Top 5 países com mais jogadores",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.xlabel("País", fontsize=11)
plt.ylabel("Quantidade de jogadores", fontsize=11)

plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.2)
plt.gca().set_axisbelow(True)

for barra in ax.patches:
    altura = barra.get_height()
    ax.annotate(
        f"{int(altura)}",
        (barra.get_x() + barra.get_width() / 2, altura),
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()
plt.show()


idade = jogadores["age"].value_counts()

print("\nQuantidade de jogadores por idade:")
print(idade.sort_index())

plt.figure(figsize=(10, 6))

ax = idade.sort_index().plot(
    kind="bar",
    color=COR_PRINCIPAL,
    edgecolor=COR_SECUNDARIA,
    width=0.8
)

plt.title(
    "Distribuição de jogadores por idade",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.xlabel("Idade", fontsize=11)
plt.ylabel("Quantidade de jogadores", fontsize=11)

plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.2)
plt.gca().set_axisbelow(True)

plt.tight_layout()
plt.show()


idade_media = jogadores["age"].mean()
print("\nIdade média dos jogadores:", idade_media)

media_controle = jogadores["ball_control"].mean()
print("\nMédia de controle de bola:", media_controle)

melhores_jogadores = jogadores.sort_values(
    by="ball_control",
    ascending=False
)

print("\n10 jogadores com maior controle de bola:")
print(melhores_jogadores[["player", "ball_control"]].head(10))

clubes = jogadores["club"].value_counts()

print("\n10 clubes com mais jogadores:")
print(clubes.head(10))


top_clubes = clubes.head(10)

plt.figure(figsize=(12, 6))

ax = top_clubes.plot(
    kind="bar",
    color=COR_PRINCIPAL,
    edgecolor=COR_SECUNDARIA,
    width=0.7
)

plt.title(
    "Top 10 clubes com mais jogadores",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.xlabel("Clube", fontsize=11)
plt.ylabel("Quantidade de jogadores", fontsize=11)

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.2)
plt.gca().set_axisbelow(True)

for barra in ax.patches:
    altura = barra.get_height()
    ax.annotate(
        f"{int(altura)}",
        (barra.get_x() + barra.get_width() / 2, altura),
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()
plt.show()



top_jogadores = melhores_jogadores.head(10)

fig, ax = plt.subplots(figsize=(12, 6), facecolor=COR_FUNDO)
ax.set_facecolor(COR_FUNDO)

barras = ax.bar(
    top_jogadores["player"],
    top_jogadores["ball_control"],
    color="#2ECC71",
    edgecolor="#1B4332",
    width=0.7
)

ax.set_title(
    "Top 10 jogadores com maior controle de bola",
    fontsize=16,
    fontweight="bold",
    color="white",
    pad=20
)

ax.set_xlabel("Jogador", color="white")
ax.set_ylabel("Controle de bola", color="white")

ax.tick_params(axis="x", colors="white", rotation=45)
ax.tick_params(axis="y", colors="white")

ax.grid(axis="y", linestyle="--", alpha=0.2)
ax.set_axisbelow(True)

for barra in barras:
    altura = barra.get_height()
    ax.annotate(
        f"{altura:.0f}",
        (barra.get_x() + barra.get_width() / 2, altura),
        ha="center",
        va="bottom",
        color="white",
        fontsize=9
    )

fig.tight_layout()
plt.show()

controle_por_idade = (
    jogadores.groupby("age")["ball_control"]
    .mean()
    .round(2)
)

print("\nMédia de controle de bola por idade:")
print(controle_por_idade)


plt.figure(figsize=(10, 6))

plt.plot(
    controle_por_idade.index,
    controle_por_idade.values,
    marker="o",
    color=COR_PRINCIPAL,
    linewidth=2
)

plt.title(
    "Média de controle de bola por idade",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.xlabel("Idade")
plt.ylabel("Média de controle de bola")

plt.grid(axis="y", linestyle="--", alpha=0.2)
plt.tight_layout()
plt.show()


quantidade_por_idade = jogadores["age"].value_counts().sort_index()

print("\nQuantidade de jogadores por idade:")
print(quantidade_por_idade)
