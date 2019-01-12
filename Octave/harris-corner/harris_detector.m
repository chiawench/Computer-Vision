input_img = imread('0133.jpeg');
if(size(input_img,3)==3)
    input_img = rgb2gray(input_img);
end
ori_im = im2double(input_img);

fx = [-1 0 1;-1 0 1;-1 0 1];          % 高斯函?一?微分，x方向(用于改?的Harris角?提取算法) 
%fx = [-2 -1 0 1 2];                 % x方向梯度算子(用于Harris角?提取算法) 
Ix = filter2(fx,ori_im);              % x方向?波 
fy = [-1 -1 -1;0 0 0;1 1 1];          % 高斯函?一?微分，y方向(用于改?的Harris角?提取算法) 
% fy = [-2;-1;0;1;2];                 % y方向梯度算子(用于Harris角?提取算法) 
Iy = filter2(fy,ori_im);              % y方向?波 

Ix2 = Ix.^2; 
Iy2 = Iy.^2; 
Ixy = Ix.*Iy; 
clear Ix; 
clear Iy; 
h= fspecial('gaussian',[7 7],2);      % ?生7*7的高斯窗函?，sigma=2 
 
Ix2 = filter2(h,Ix2); 
Iy2 = filter2(h,Iy2); 
Ixy = filter2(h,Ixy); 

[height,width] = size(ori_im); 
result = zeros(height,width);         % ??角?位置，角??result的值?1 
R = zeros(height,width); 

Rmax = 0;                              % ?像中最大的R值 
for i = 1:height 
    for j = 1:width 
        M = [Ix2(i,j) Ixy(i,j);Ixy(i,j) Iy2(i,j)];       
        R(i,j) = det(M)-0.06*(trace(M))^2;          
        if R(i,j) > Rmax 
            Rmax = R(i,j); 
        end 
    end
end
 
cnt = 0; %角???
for i = 2:height-1 
    for j = 2:width-1 
        % ?行非极大抑制，窗口大小3*3 
        if R(i,j) > 0.01*Rmax && R(i,j) > R(i-1,j-1) && R(i,j) > R(i-1,j) && R(i,j) > R(i-1,j+1) && R(i,j) > R(i,j-1) && R(i,j) > R(i,j+1) && R(i,j) > R(i+1,j-1) && R(i,j) > R(i+1,j) && R(i,j) > R(i+1,j+1) 
            result(i,j) = 1; 
            cnt = cnt+1; 
        end
    end
end
 
[posc, posr] = find(result == 1); 
disp(cnt);                 % ?示角??? 
imshow(ori_im); 
hold on; 
plot(posr,posc,'r+'); 
