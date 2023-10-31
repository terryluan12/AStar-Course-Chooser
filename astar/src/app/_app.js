import '../styles/global.css';
import 'bootstrap/dist/css/bootstrap.css';
import {Fredoka} from 'next/font/google'

const fred = Fredoka({subsets: ["latin"], weight: ["400", "500", "600", "700", "800", "900"], display: 'swap',});

export default function App({ Component, pageProps }) {
    return <main className={fred.className}><Component {...pageProps} /></main>;
}