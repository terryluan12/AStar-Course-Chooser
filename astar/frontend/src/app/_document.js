import Document, { Head, Main, NextScript } from 'next/document'

export default class MyDocument extends Document {
  render() {
    return (
      <html>
        <Head>
          <link
            rel="stylesheet"
            href={`${this.props.__NEXT_DATA__.assetPrefix}/_next/static/style.css`}
          />
        <link rel="icon" href="/favicon.ico" />
        
        <meta name="theme-color" content="#000000" />
        <meta
        name="description"
        content="A course finder allowing students to choose courses"
        />
        <title>AStar Chooser</title>

        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </html>
    )
  }
}