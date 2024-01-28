#include <iostream>
using namespace std;
bool gameover;
int height = 20, width = 20;
int x, y;
int fruitx, fruity;
int sco=0;
enum direct
{
    stop = 0,
    u,
    l,
    r,
    dow
};
direct ion;

void setup()
{
    gameover = false;
    x = width / 2 +1;
    y = height / 2 +1;
    fruitx = rand() % width;
    fruity = rand() % height;
}
void input()
{
    system("stty raw");
    int c = getchar();
    switch (c)
    {
    case 97:
        ion = l;
        break;
    case 100:
        ion = r;
        break;
    case 119:
        ion = u;
        break;
    case 115:
        ion = dow;
        break;
    case 120:
        gameover = true;
        break;
    }
    system("stty cooked");
    
}
void draw()
{
    system("clear");
    for (int i = 0; i < width+2; i++)
    {
        cout << '#';
    }
    cout << endl;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width+2; j++)
        {
            if (j == 0 || j == width +1)
            {
                cout << "#";
            }
            else if (j == x && i == y)
            {
                cout << "O";
            }
            else if (j == fruitx && i == fruity)
            {
                cout << "f";
            }
            else
            {
                cout << " ";
            }
        }
        cout << endl;
    }
    for (int j = 0; j < width+2; j++)
    {
        cout << "#";
    }
    cout<<endl;
    cout<<sco<<endl;
}
void move()
{
    switch (ion)
    {
    case l:
        x--;
        break;
    case r:
        x++;
        break;
    case u:
        y--;
        break;
    case dow:
        y++;
        break;

    default:

        break;
    }
    if(x>width||x<0||y<0||y>height){
        gameover=true;
    }
    if(x==fruitx&&y==fruity){
        sco++;
  
    fruitx = rand() %( width+2);
    fruity = rand() % (height+2);
    if(fruitx==0||fruitx==width+1){
        fruitx=width/2;

    }
      if(fruity==0||fruity==height+1){
        fruity=height/2;

    }

    }
}

int main()
{
    setup();

    while (!gameover)
    {
        draw();
        input();
        move();
    }
}
