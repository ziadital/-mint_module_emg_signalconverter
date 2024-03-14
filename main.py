namespace EMGConversion {
    const bufferSize = 20; // Größe des Puffers für die Signalakkumulation
    let signalBuffer: number[] = [];

    /**
     * Fügt ein neues Signal zum Puffer hinzu und gibt den Mittelwert zurück, wenn der Puffer voll ist
     * @param signal Das neue Signal
     * @returns Der Mittelwert der gesammelten Signale oder undefined, wenn der Puffer nicht voll ist
     */
    //% block="Füge Signal hinzu und gib Mittelwert aus $signal"
    //% signal.min=0 signal.max=1023
    export function addSignalAndReturnAverage(signal: number): number | undefined {
        signalBuffer.push(signal); // Füge das Signal zum Puffer hinzu

        if (signalBuffer.length === bufferSize) {
            // Berechne den Mittelwert, wenn der Puffer voll ist
            const sum = signalBuffer.reduce((acc, val) => acc + val, 0);
            const average = sum / bufferSize;
            signalBuffer = []; // Leere den Puffer für das nächste Mal
            return average;
        }

        return undefined; // Der Puffer ist noch nicht voll, daher geben wir undefined zurück
    }
}
