sizes =[];
for i = 0:11
    num = i * 5;
    fileName = strcat(num2str(num),'.json');
    fid=fopen(fileName);
    raw=fread(fid,inf);
    str=char(raw');
    fclose(fid);
    data=jsondecode(str);
    a=struct2cell(data);
    
    sizes=[ length(fieldnames(a{1})) sizes] ;
    
    
end
x = linspace(0,55,12);
    bar(x,sizes)
    xlabel('minutes after 13:25')
    ylabel('number of devices connected to wifi')
    title('Wifi scanning Sunday')
