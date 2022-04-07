import gif from '../fishtank.gif';

export default function Fishtank() {
    return (
        <main style={{
            height: '100%',
            position: 'absolute',
            left: '0',
            width: '100%',
            overflow: 'hidden',
            backgroundColor: 'black',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
        }}>
            <img src={gif} alt="Fishtank GIF" />
        </main>
    );
}
