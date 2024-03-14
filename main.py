namespace EMGConversion {
    const windowDurationMs = 1000; // Zeitfenster in Millisekunden
    const samplingRateHz = 100; // Annahme einer Abtastfrequenz von 100 Hz
    const bufferSize = windowDurationMs * samplingRateHz / 1000; // Größe des Puffers basierend auf der Abtastfrequenz und der Zeitfensterdauer
    let signalBuffer: number[] = [];
    let timer: number; // Timer-ID für die Signalerfassung

    /**
     * Startet die Signalerfassung
     */
    //% block="Starte Erfassung"
    export function startSampling(): void {
        signalBuffer = []; // Leeren des Puffers
        timer = control.timer1.runInParallel(() => {
            stopSampling(); // Stoppt die Erfassung nach Ablauf der Zeit
        }, windowDurationMs);
    }

    /**
     * Stoppt die Signalerfassung und berechnet den RMS-Wert
     */
    //% block="Stoppe Erfassung und berechne RMS"
    export function stopSampling(): void {
        control.timer1.pause(timer); // Stoppt den Timer
        const rms = calculateRMS(); // Berechnet den RMS-Wert
        control.timer1.reset(timer); // Setzt den Timer zurück
        return rms;
    }

    /**
     * Berechnet den Mittelwert aus den im Puffer gespeicherten Signalen
     * @returns Der Mittelwert der gesammelten Signale
     */
    function calculateRMS(): number {
        if (signalBuffer.length == 0) {
            return 0; // Falls kein Signal erfasst wurde, gebe 0 zurück
        }
        // Berechnet die Summe der Signale im Puffer
        const sum = signalBuffer.reduce((acc, val) => acc + val, 0);
        // Berechnet den Mittelwert
        const mean = sum / signalBuffer.length;
        return mean;
    }

    /**
     * Fügt ein neues Signal zum Puffer hinzu
     * @param signal Das neue Signal
     */
    //% block="Füge Signal hinzu $signal"
    //% signal.min=0 signal.max=1023
    export function addSignal(signal: number): void {
        if (signalBuffer.length < bufferSize) {
            signalBuffer.push(signal); // Fügt das Signal hinzu, wenn der Puffer nicht voll ist
        }
    }
}
