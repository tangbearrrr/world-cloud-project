import Head from 'next/head'

const SearchBar = () => {
  return (
    <form>
      <label for="search">Search</label>
      <input id="search" type="search" pattern=".*\S.*" required />
      <span class="caret"></span>
    </form>
  )
}

export default function Home() {
  return (
    <div className="container">
      <Head>
        <title>World Cloud Project</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className="title">
          Word Cloud Project
        </h1>

        <p className="description">
          Get started here <SearchBar />
        </p>
      </main>
    </div>
  )
}
