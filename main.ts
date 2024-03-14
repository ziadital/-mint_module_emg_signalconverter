namespace EMGConversion {
    let accumulatedSum = 0;
    let count = 0;

    /**
     * Filters, rectifies, and calculates the RMS of the EMG signal
     * @param signal The raw EMG signal
     * @returns The RMS of the EMG signal
     */
    //% block="Filter RAW Signal $signal"
    //% signal.min=0 signal.max=1023
    export function convertFilterRectifyAndCalculateRMS(signal: number): number {
        // Filter and rectify the signal (in this example, the filter is just taking the absolute value)
        const filteredSignal = Math.abs(signal);

        // Accumulate the sum of squares
        accumulatedSum += filteredSignal * filteredSignal;
        count++;

        // Calculate RMS (Root Mean Square) value
        const rms = Math.sqrt(accumulatedSum / count);

        return rms;
    }
}
