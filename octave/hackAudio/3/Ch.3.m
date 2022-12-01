#### Example 3.1-2 - audioread, sound
##fn = '/home/danny/octave/Hack_Audio/Ch.3/sw440Hz.wav';
##[sw,Fs] = audioread(fn);
##sound(sw,Fs);
##
##
#### Example 3.3 - audiowrite
##fnIn = '/home/danny/octave/Hack_Audio/Ch.3/sw440Hz.wav';
##[sw,Fs] = audioread(fnIn);
##fnOut = '/home/danny/octave/Hack_Audio/Ch.3/testSignal.wav';
##audiowrite(fnOut,sw,Fs);
##
##
#### Example 3.4 - audioinfo
##fn = '/home/danny/octave/Hack_Audio/Ch.3/testSignal.wav';
##info = audioinfo(fn)
##
##
##
#### Example 3.5 - Indexing arrays
##V = [ 20 21 22 23 24 25 ];
##V(1), V(3), V(6), V(end)
##V(2) = 31;
##V
##M = [ 11 12 ; 13 14 ; 15 16 ];
##M(1,end), M(end,2)
##[sw,Fs] = audioread(fn);
##sw(1), sw(2), sw(3), sw(4)
##
##
##
#### Example 3.6
##vv = V(:)
##vv(:)
##vv = V(2:3)
##vv = V(4:end)
##V(1:2) = [41 42]
##M
##mm = M(:,1)
##mm = M(2,:)
##mm = M(:,:)
##M(2,:) = [41 42]
##mm = M(2:3,1:2)  %%mm is M, rows 2/3, columns 1/2
##mm = M(1:2,2)
##[sw,Fs] = audioread(fn);
##plot(sw(1:201),'r--','LineWidth',2)
##
##
##
#### Example 3.7 - Signal splice
##[x,Fs] = audioread('/home/danny/Code/Octave/Hack_Audio/Ch.3/Vocal.wav');
##figure(1)
##plot(x)
##
##edit1 = x(1:47609,1);
##figure(2)
##plot(edit1,'b','LineWidth',1.5);
##sound(edit1,Fs);
##
##edit2 = x(123252:end,1);
##figure(3)
##plot(edit2);
##sound(edit2,Fs);
##
##edit3 = [edit1 ; edit2];
##sound(edit3,Fs);
##
##
##
## Example 3.8 - Time-reversing a vocal recording
##fn = '/home/danny/Code/Octave/Hack_Audio/Ch.3/Vocal.wav'
##fn = '/home/danny/octave/Hack_Audio/Ch.3/04.Waterfall.mp3'
##[x,Fs] = audioread(fn);
##plot(x);
##xReverse = x(end:-1:1);
##sound(xReverse,Fs);
##plot(xReverse);
##
##
##
#### Example 3.9 - Efficient array creation
##vec1 = 6:10
##vec2 = [ -4:3 ]
##vec3 = 1:2:11
##vec4 = 1:2:10
##vec5 = 1:3:2
##vecErr = [ 3:1 ]
##vec6 = 3:-1:1
##Ts = 1/48000;
##t = 0:Ts:1
##
##
##
#### Example 3.10 - Function: linspace
##vec7 = linspace(10,14,5)
##vec8 = linspace(10,13,5)
##vec9 = linspace(13,10,5)
##vec10 = linspace(0,100,5)
##mat5 = [ 1:2:11 ; linspace(1,11,6) ]
##
##
##
#### Example 3.11 - Function: logspace
##vec11 = logspace(0,2,10)
##vec12 = logspace(1,4,20)
##
##
##
#### Example 3.12 - Arrays with predefined values
##ones(3,1)
##zeros(2,3)
##eye(4)
##
##
##
#### Example 3.13 - Array transpose operation
##x = [ 1 2 3 ];
##traVec = x.'
##w = [ 1 2 3 ; 4 5 6 ]
##traMat = w.'
##colVec = x(:)
##colVec(:)
##w(:)
##
##
##
#### Example 3.14 - Determining dimensions of arrays
##x = ones(3,2)
##[row,col] = size(x)
##size(x,1)
##size(x,2)
##length(x)
##y = zeros(2,3)
##length(y)
##
##fn = '/home/danny/Code/Octave/Hack_Audio/Ch.3/sw440Hz.wav';
##[sw,Fs] = audioread(fn)
##[row,col] = size(fn)
##size(fn,1)
##size(fn,2)
##
##
##
#### Example 3.15 - Plotting audio signals
fn = '/home/danny/code/octave/hackAudio/3/sw20Hz.wav'
[sw,Fs] = audioread(fn);
figure(1)
plot(sw);
xlabel('Sample Number');
axis([0 45000 -1.5 1.5]);
Ts = 1/Fs;
t = 0:Ts:1;
figure(2)
plot(t,sw);
xlabel('Time (sec.)');
axis([0 1.1 -1.5 1.5]);