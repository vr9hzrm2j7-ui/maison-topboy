from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maison Topboy | Parfums de luxe</title>
    <meta name="description" content="Découvrez la collection de parfums Maison Topboy au Sénégal.">

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background: #0b0b0b;
            color: #f8f4eb;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }

        :root {
            --or: #d5b36a;
            --noir: #0b0b0b;
            --carte: #171614;
            --texte: #c8c2b7;
        }

        header {
            padding: 20px 7%;
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

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 22px;
            font-size: 14px;
        }

        nav a:hover {
            color: var(--or);
        }
        }

        .hero {
            min-height: 470px;
            padding: 90px 7%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            background:
                radial-gradient(ellipse at 80% 40%, #4b3920 0%, #201a12 28%, #0b0b0b 70%);
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

        .hero p {
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

        .produits {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 24px;
        }

        .produit {
            background: var(--carte);
            border: 1px solid #30291d;
            border-radius: 5px;
            overflow: hidden;
            transition: transform 0.2s, border-color 0.2s;
        }

        .produit:hover {
            transform: translateY(-5px);
            border-color: var(--or);
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
            padding: 22px;
        }

        .categorie {
            color: var(--or);
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .produit h3 {
            font-family: Georgia, serif;
            font-size: 22px;
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
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 18px;
        }

        .commander {
            display: block;
            text-align: center;
            padding: 11px;
            border: 1px solid var(--or);
            color: var(--or);
            text-decoration: none;
            border-radius: 3px;
            font-weight: bold;
        }

        .commander:hover {
            background: var(--or);
            color: #111;
        }

        .avantages {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
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

        @media (max-width: 600px) {
            header {
                flex-direction: column;
                text-align: center;
            }

            nav a {
                margin: 0 8px;
            }

            .hero {
                min-height: 400px;
                padding: 65px 7%;
            }

            .section {
                padding: 45px 6%;
            }

            .section-titre h2 {
                font-size: 29px;
            }
        }
    </style>
</head>

<body>
    <header>
       <a href="#" class="logo-image">
       <img src="{{ url_for('static', filename='images/logo_maison_topboy.jpeg') }}" alt="Maison Topboy">
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
            <a class="bouton" href="#collection">DÉCOUVRIR LA COLLECTION</a>
        </section>

        <section class="section" id="collection">
            <div class="section-titre">
                <p>La sélection Maison Topboy</p>
                <h2>Nos parfums</h2>
            </div>

            <div class="produits">
                <article class="produit">
                    <img class="photo"
     src="{{ url_for('static', filename='images/parfum1.jpg') }}"
     alt="IGNITE OUD">
                    <div class="produit-contenu">
                        <p class="categorie">Boisé · Mixte</p>
                        <h3>IGNITE OUD </h3>
                        <p class="description">
                            Une ambiance boisée, profonde et raffinée.
                        </p>
                        <p class="prix">20 000 FCFA</p>
                        <a class="commander"
                           href="https://wa.me/221755256145?text=Bonjour%20Maison%20Topboy%2C%20je%20souhaite%20commander%20Oud%20Prestige">
                            Commander sur WhatsApp
                        </a>
                    </div>
                </article>

                <article class="produit">
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
                           href="https://wa.me/221755256145?text=Bonjour%20Maison%20Topboy%2C%20je%20souhaite%20commander%20Rose%20Royale">
                            Commander sur WhatsApp
                        </a>
                    </div>
                </article>

                <article class="produit">
                    <img class="photo"
     src="{{ url_for('static', filename='images/parfum3.jpg') }}"
     alt="BADE’E AL OUD">
                    <div class="produit-contenu">
                        <p class="categorie">Élégant · Mixte</p>
                        <h3>BADE'E AL OUD</h3>
                        <p class="description">
                            Une senteur sophistiquée pour toutes les occasions.
                        </p>
                        <p class="prix">15 000 FCFA</p>
                        <a class="commander"
                           href="https://wa.me/221755256145?text=Bonjour%20Maison%20Topboy%2C%20je%20souhaite%20commander%20Elegance">
                            Commander sur WhatsApp
                        </a>
                    </div>
                </article>
<article class="produit">
    <img class="photo"
         src="{{ url_for('static', filename='images/parfum4.jpg') }}"
         alt="Parfum OUD AL-MALIK">

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
            <p>Écrivez-nous pour connaître les disponibilités et la livraison.</p>
            <a class="bouton"
               href="https://wa.me/221XXXXXXXXX?text=Bonjour%20Maison%20Topboy">
                NOUS CONTACTER
            </a>
        </section>
    </main>

    <footer>
        <strong>MAISON TOPBOY</strong>
        <p>Le luxe au quotidien.</p>
        <p>© 2026 Maison Topboy · Sénégal</p>
    </footer>
</body>
</html>
"""

@app.route("/")
def accueil():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
