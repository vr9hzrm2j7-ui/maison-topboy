from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maison Topboy | Boutique de parfums au Sénégal</title>
   <meta name="description" content="Découvrez Maison Topboy, votre boutique de parfums au Sénégal. Explorez notre sélection de fragrances élégantes et commandez facilement sur WhatsApp.">
    <meta name="google-site-verification" content="xjOwkDKQOgRytaN2qGCJepC1nWpqbG8sAsiTGKXuWL0" />

    <style>
        :root {
            --or: #d5b36a;
            --noir: #0b0b0b;
            --carte: #171614;
            --texte: #c8c2b7;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background: var(--noir);
            color: #f8f4eb;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }

        header {
            padding: 18px 7%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            border-bottom: 1px solid #393020;
            background: #080808;
        }

        .logo-image {
            display: inline-flex;
            align-items: center;
            flex-shrink: 0;
        }

        .logo-image img {
            display: block;
            width: 180px;
            max-width: 100%;
            height: auto;
        }

        nav {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 22px;
        }

        nav a {
            color: white;
            text-decoration: none;
            font-size: 14px;
        }

        nav a:hover {
            color: var(--or);
        }

        .hero {
            min-height: 440px;
            padding: 80px 7%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            background:
                radial-gradient(ellipse at 80% 40%,
                #4b3920 0%, #201a12 28%, #0b0b0b 70%);
        }

        .surtitle {
            color: var(--or);
            text-transform: uppercase;
            letter-spacing: 4px;
            font-size: 12px;
            margin-bottom: 20px;
        }

        .hero h1 {
            font-family: Georgia, serif;
            font-size: clamp(38px, 7vw, 72px);
            line-height: 1.1;
            max-width: 700px;
            margin-bottom: 22px;
        }

        .hero h1 span {
            color: var(--or);
        }

        .hero p:not(.surtitle) {
            max-width: 500px;
            color: var(--texte);
            margin-bottom: 30px;
        }

        .bouton {
            display: inline-block;
            padding: 13px 24px;
            background: var(--or);
            color: #111;
            border: 1px solid var(--or);
            text-decoration: none;
            font-weight: bold;
            border-radius: 3px;
            transition: 0.2s;
        }

        .bouton:hover {
            background: transparent;
            color: var(--or);
        }

        .section {
            padding: 65px 7%;
        }

        .section-titre {
            text-align: center;
            margin-bottom: 35px;
        }

        .section-titre p {
            color: var(--or);
            font-size: 12px;
            letter-spacing: 3px;
            text-transform: uppercase;
        }

        .section-titre h2 {
            font-family: Georgia, serif;
            font-size: 35px;
            margin-top: 8px;
        }

        .outils-collection {
            max-width: 720px;
            margin: 0 auto 30px;
        }

        .recherche-parfum {
            display: block;
            width: 100%;
            padding: 14px 17px;
            border: 1px solid var(--or);
            border-radius: 5px;
            background: var(--carte);
            color: #f8f4eb;
            font-size: 16px;
        }

        .recherche-parfum::placeholder {
            color: #aaa294;
        }

        .recherche-parfum:focus {
            outline: 2px solid #d5b36a66;
            outline-offset: 2px;
        }

        .filtres-parfums {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
            margin-top: 18px;
        }

        .filtre-parfum {
            padding: 9px 16px;
            background: transparent;
            color: var(--or);
            border: 1px solid var(--or);
            border-radius: 25px;
            cursor: pointer;
            font-size: 13px;
        }

        .filtre-parfum:hover,
        .filtre-parfum.actif {
            background: var(--or);
            color: #111;
        }

        .produits {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 24px;
        }

        .produit {
            min-width: 0;
            background: var(--carte);
            border: 1px solid #30291d;
            border-radius: 5px;
            overflow: hidden;
            transition: transform 0.2s, border-color 0.2s;
        }

        .produit:hover {
            transform: translateY(-4px);
            border-color: var(--or);
        }

        .produit.masque {
            display: none;
        }

        .photo {
            width: 100%;
            height: 230px;
            display: block;
            object-fit: contain;
            padding: 20px;
            background: linear-gradient(145deg, #302719, #121212);
        }

        .produit-contenu {
            padding: 20px;
        }

        .categorie {
            color: var(--or);
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }

        .produit h3 {
            font-family: Georgia, serif;
            font-size: 21px;
            overflow-wrap: anywhere;
            margin: 8px 0;
        }

        .description {
            color: var(--texte);
            font-size: 14px;
            min-height: 46px;
            margin-bottom: 15px;
        }

        .prix {
            color: var(--or);
            font-size: 21px;
            font-weight: bold;
            margin-bottom: 18px;
        }

        .commander {
            display: block;
            text-align: center;
            padding: 11px 8px;
            border: 1px solid var(--or);
            color: var(--or);
            text-decoration: none;
            border-radius: 3px;
            font-weight: bold;
            font-size: 13px;
        }

        .commander:hover {
            background: var(--or);
            color: #111;
        }

        .message-vide {
            display: none;
            text-align: center;
            color: var(--texte);
            padding: 25px 10px;
        }

        .message-vide.visible {
            display: block;
        }

        .avantages {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 25px;
            text-align: center;
            background: #12110f;
        }

        .avantage {
            padding: 20px;
        }

        .avantage .icone {
            font-size: 30px;
            margin-bottom: 10px;
        }

        .avantage h3 {
            color: var(--or);
            margin-bottom: 7px;
        }

        .avantage p {
            color: var(--texte);
            font-size: 14px;
        }

        .contact {
            text-align: center;
            background: linear-gradient(135deg, #241d12, #0b0b0b);
        }

        .contact p {
            color: var(--texte);
            margin: 12px 0 25px;
        }

        footer {
            padding: 30px 7%;
            text-align: center;
            border-top: 1px solid #393020;
            color: var(--texte);
            font-size: 13px;
        }

        footer strong {
            color: var(--or);
            letter-spacing: 2px;
        }

        @media (max-width: 1000px) {
            .produits {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 600px) {
            header {
                flex-direction: column;
                text-align: center;
                padding: 18px 5%;
                gap: 14px;
            }

            .logo-image img {
                width: 150px;
            }

            nav {
                justify-content: center;
                gap: 18px;
            }

            nav a {
                font-size: 13px;
            }

            .hero {
                min-height: 380px;
                padding: 55px 6%;
            }

            .section {
                padding: 45px 5%;
            }

            .section-titre h2 {
                font-size: 29px;
            }

            .produits {
                gap: 12px;
            }

            .photo {
                height: 175px;
                padding: 12px;
            }

            .produit-contenu {
                padding: 12px;
            }

            .produit h3 {
                font-size: 17px;
            }

            .description {
                font-size: 12px;
                min-height: 0;
            }

            .prix {
                font-size: 17px;
            }

            .commander {
                font-size: 12px;
                padding: 10px 5px;
            }

            .avantages {
                grid-template-columns: 1fr;
                gap: 8px;
            }

            .filtre-parfum {
                padding: 8px 12px;
            }
        }

        @media (max-width: 360px) {
            .produits {
                grid-template-columns: 1fr;
            }

            .photo {
                height: 230px;
            }
        }
    </style>
</head>

<body>
    <header>
        <a href="#" class="logo-image">
            <img
                src="{{ url_for('static', filename='images/logo_maison_topboy.jpeg') }}"
                alt="Maison Topboy"
            >
        </a>

        <nav>
            <a href="#">Accueil</a>
            <a href="#collection">Collection</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>

    <main>
        <section class="hero">
            <p class="surtitle">L'art de la parfumerie</p>
            <h1>Votre signature.<br><span>Votre parfum.</span></h1>
            <p>
                Découvrez une collection de fragrances élégantes
                pour révéler votre personnalité, chaque jour.
            </p>
            <a class="bouton" href="#collection">
                DÉCOUVRIR LA COLLECTION
            </a>
        </section>

        <section class="section" id="collection">
            <div class="section-titre">
                <p>La sélection Maison Topboy</p>
                <h2>Nos parfums</h2>
            </div>

            <div class="outils-collection">
                <input
                    type="search"
                    id="rechercheParfum"
                    class="recherche-parfum"
                    placeholder="Rechercher un parfum..."
                    aria-label="Rechercher un parfum"
                >

                <div class="filtres-parfums"
                     aria-label="Catégories de parfums">
                    <button type="button"
                            class="filtre-parfum actif"
                            data-filtre="tous">Tous</button>
                    <button type="button"
                            class="filtre-parfum"
                            data-filtre="mixte">Mixte</button>
                    <button type="button"
                            class="filtre-parfum"
                            data-filtre="oud">Oud</button>
                    <button type="button"
                            class="filtre-parfum"
                            data-filtre="boise">Boisé</button>
                    <button type="button"
                            class="filtre-parfum"
                            data-filtre="floral">Floral</button>
                </div>
            </div>

            <div class="produits">
                <article class="produit"
                         data-categories="mixte oud boise">
                    <img class="photo"
                         src="{{ url_for('static', filename='images/parfum1.jpg') }}"
                         alt="IGNITE OUD">
                    <div class="produit-contenu">
                        <p class="categorie">Boisé · mixte</p>
                        <h3>IGNITE OUD</h3>
                        <p class="description">
                            Une ambiance boisée, profonde et raffinée.
                        </p>
                        <p class="prix">20 000 FCFA</p>
                        <a class="commander"
                           href="https://wa.me/221755256145?text=Bonjour%20Maison%20Topboy%2C%20je%20souhaite%20commander%20IGNITE%20OUD">
                            Commander sur WhatsApp
                        </a>
                    </div>
                </article>

                <article class="produit"
                         data-categories="mixte oud floral">
                    <img class="photo"
                         src="{{ url_for('static', filename='images/parfum2.jpg') }}"
                         alt="TOM FORD OUD">
                    <div class="produit-contenu">
                        <p class="categorie">Floral · mixte</p>
                        <h3>TOM FORD OUD</h3>
                        <p class="description">
                            Une fragrance florale, douce et délicate.
                        </p>
                        <p class="prix">12 000 FCFA</p>
                        <a class="commander"
                           href="https://wa.me/221755256145?text=Bonjour%20Maison%20Topboy%2C%20je%20souhaite%20commander%20TOM%20FORD%20OUD">
                            Commander sur WhatsApp
                        </a>
                    </div>
                </article>

                <article class="produit"
                         data-categories="mixte oud">
                    <img class="photo"
                         src="{{ url_for('static', filename='images/parfum3.jpg') }}"
                         alt="BADE'E AL OUD">
                    <div class="produit-contenu">
                        <p class="categorie">Élégant · Mixte</p>
                        <h3>BADE'E AL OUD</h3>
                        <p class="description">
                            Une senteur sophistiquée pour toutes les occasions.
                        </p>
                        <p class="prix">15 000 FCFA</p>
                        <a class="commander"
                           href="https://wa.me/221755256145?text=Bonjour%20Maison%20Topboy%2C%20je%20souhaite%20commander%20BADE%27E%20AL%20OUD">
                            Commander sur WhatsApp
                        </a>
                    </div>
                </article>

                <article class="produit"
                         data-categories="oud">
                    <img class="photo"
                         src="{{ url_for('static', filename='images/parfum4.jpg') }}"
                         alt="OUD AL-MALIK">
                    <div class="produit-contenu">
                        <p class="categorie">Parfum · Oud</p>
                        <h3>OUD AL-MALIK</h3>
                        <p class="description">
                            Une fragrance élégante pour le quotidien.
                        </p>
                        <p class="prix">10 000 FCFA</p>
                        <a class="commander"
                           href="https://wa.me/221755256145?text=Bonjour%20Maison%20Topboy%2C%20je%20souhaite%20commander%20OUD%20AL-MALIK">
                            Commander sur WhatsApp
                        </a>
                    </div>
                </article>
            </div>

            <p class="message-vide" id="messageVide">
                Aucun parfum trouvé.
            </p>
        </section>

        <section class="section avantages">
            <div class="avantage">
                <div class="icone">✦</div>
                <h3>Style & élégance</h3>
                <p>Une sélection pensée pour tous les goûts.</p>
            </div>
            <div class="avantage">
                <div class="icone">♡</div>
                <h3>Pour elle et lui</h3>
                <p>Des fragrances pour chaque personnalité.</p>
            </div>
            <div class="avantage">
                <div class="icone">✉</div>
                <h3>Commande facile</h3>
                <p>Contactez-nous pour commander au Sénégal.</p>
            </div>
        </section>

        <section class="section contact" id="contact">
            <div class="section-titre">
                <p>Restons en contact</p>
                <h2>Un parfum vous intéresse ?</h2>
            </div>
            <p>
                Écrivez-nous pour connaître les disponibilités
                et la livraison.
            </p>
            <a class="bouton"
               href="https://wa.me/221755256145?text=Bonjour%20Maison%20Topboy">
                NOUS CONTACTER
            </a>
        </section>
    </main>

    <footer>
        <strong>MAISON TOPBOY</strong>
        <p>Le luxe au quotidien.</p>
        <p>© 2026 Maison Topboy · Sénégal</p>
    </footer>

    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const recherche = document.getElementById("rechercheParfum");
            const boutons = document.querySelectorAll(".filtre-parfum");
            const produits = document.querySelectorAll(".produit");
            const messageVide = document.getElementById("messageVide");

            let categorieActive = "tous";

            function normaliser(texte) {
                return texte
                    .toLocaleLowerCase("fr")
                    .normalize("NFD")
                    .replace(/[\\u0300-\\u036f]/g, "");
            }

            function filtrerProduits() {
                const terme = normaliser(recherche.value.trim());
                let nombreVisible = 0;

                produits.forEach(function (produit) {
                    const texte = normaliser(produit.textContent);
                    const categories =
                        (produit.dataset.categories || "").split(/\\s+/);

                    const correspondRecherche = texte.includes(terme);
                    const correspondCategorie =
                        categorieActive === "tous" ||
                        categories.includes(categorieActive);

                    const visible =
                        correspondRecherche && correspondCategorie;

                    produit.classList.toggle("masque", !visible);

                    if (visible) {
                        nombreVisible++;
                    }
                });

                messageVide.classList.toggle(
                    "visible",
                    nombreVisible === 0
                );
            }

            recherche.addEventListener("input", filtrerProduits);

            boutons.forEach(function (bouton) {
                bouton.addEventListener("click", function () {
                    categorieActive = bouton.dataset.filtre;

                    boutons.forEach(function (autreBouton) {
                        autreBouton.classList.toggle(
                            "actif",
                            autreBouton === bouton
                        );
                    });

                    filtrerProduits();
                });
            });
        });
    </script>
</body>
</html>
"""

@app.route("/")
def accueil():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
