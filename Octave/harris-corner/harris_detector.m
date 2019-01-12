input_img = imread('0133.jpeg');
if(size(input_img,3)==3)
    input_img = rgb2gray(input_img);
end
ori_im = im2double(input_img);

fx = [-1 0 1;-1 0 1;-1 0 1];          % ������?�@?�L���Ax��V(�Τ_��?��Harris��?������k) 
%fx = [-2 -1 0 1 2];                 % x��V��׺�l(�Τ_Harris��?������k) 
Ix = filter2(fx,ori_im);              % x��V?�i 
fy = [-1 -1 -1;0 0 0;1 1 1];          % ������?�@?�L���Ay��V(�Τ_��?��Harris��?������k) 
% fy = [-2;-1;0;1;2];                 % y��V��׺�l(�Τ_Harris��?������k) 
Iy = filter2(fy,ori_im);              % y��V?�i 

Ix2 = Ix.^2; 
Iy2 = Iy.^2; 
Ixy = Ix.*Iy; 
clear Ix; 
clear Iy; 
h= fspecial('gaussian',[7 7],2);      % ?��7*7����������?�Asigma=2 
 
Ix2 = filter2(h,Ix2); 
Iy2 = filter2(h,Iy2); 
Ixy = filter2(h,Ixy); 

[height,width] = size(ori_im); 
result = zeros(height,width);         % ??��?��m�A��??result����?1 
R = zeros(height,width); 

Rmax = 0;                              % ?�����̤j��R�� 
for i = 1:height 
    for j = 1:width 
        M = [Ix2(i,j) Ixy(i,j);Ixy(i,j) Iy2(i,j)];       
        R(i,j) = det(M)-0.06*(trace(M))^2;          
        if R(i,j) > Rmax 
            Rmax = R(i,j); 
        end 
    end
end
 
cnt = 0; %��???
for i = 2:height-1 
    for j = 2:width-1 
        % ?��D��j���A���f�j�p3*3 
        if R(i,j) > 0.01*Rmax && R(i,j) > R(i-1,j-1) && R(i,j) > R(i-1,j) && R(i,j) > R(i-1,j+1) && R(i,j) > R(i,j-1) && R(i,j) > R(i,j+1) && R(i,j) > R(i+1,j-1) && R(i,j) > R(i+1,j) && R(i,j) > R(i+1,j+1) 
            result(i,j) = 1; 
            cnt = cnt+1; 
        end
    end
end
 
[posc, posr] = find(result == 1); 
disp(cnt);                 % ?�ܨ�??? 
imshow(ori_im); 
hold on; 
plot(posr,posc,'r+'); 
