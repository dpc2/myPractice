## Script to reverse the Stone Roses song Don't Stop

fn = '/home/danny/code/octave/hackAudio/3/dontStop.wav'
[x,Fs] = audioread(fn);
figure(1)
plot(x);
xReverse = x(end:-1:1);
audiowrite("tnodPots.wav",xReverse,Fs);