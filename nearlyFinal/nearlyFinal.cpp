#include <iostream>
#include <set>
#include <tuple>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <map>

#include <fstream>

using namespace cv;
using namespace std;


string a[45];
vector <string> FoCoBo[45];
vector < tuple< unsigned char, unsigned char, unsigned char > > bangMau[45];
vector < tuple< unsigned char, unsigned char, unsigned char > > mau;



struct ob
{
	int ID;
	int x;
};
bool dk2(ob A, ob B)
{
	
	return A.x > B.x;
}
void taoBangPhoiMau()
{
	int demi = 0;
	for (char i = '0'; i <= '3'; i++)
		for(char j = '0'; j <= '9'; j++)
			{
			//"E:\temp\bangPhoiMau\pallete\bang01.png"
				a[demi] = "E:\\temp\\bangPhoiMau\\pallete\\bang";
				a[demi] += i;
				a[demi] += j;
				a[demi] += ".png";
				demi++;
			}


	set < tuple< unsigned char, unsigned char, unsigned char > > se;
	set < tuple< unsigned char, unsigned char, unsigned char > > ::iterator ie;





	for (int I = 0; I < 40; I++)
	{
		Mat image1 = imread(a[I], IMREAD_COLOR);
		set < tuple< unsigned char, unsigned char, unsigned char > > sem;
		//khoong caafn resize ?

		//imshow("Image", image1);

		//waitKey(0);


		for (int i = 0; i < image1.rows; i++)
		{
			for (int j = 0; j < image1.cols; j++)
			{
				Vec3b bgrPixel = image1.at<Vec3b>(i, j);

				sem.insert({ bgrPixel[0] - (bgrPixel[0] % 25), bgrPixel[1] - (bgrPixel[1] % 25), bgrPixel[2] - (bgrPixel[2] % 25) }); // thu nhor

			}
		}

		for (ie = sem.begin(); ie != sem.end(); ie++)
		{
			tuple< unsigned char, unsigned char, unsigned char > tem = *ie;

			bangMau[I].push_back(tem);
			se.insert(tem);
		}

	}

	for (ie = se.begin(); ie != se.end(); ie++)
		mau.push_back(*ie);
	
}
void xuLyMotAnh(Mat& image1)
{
	

	for (int i = 0; i < image1.rows; i++)
	{
		for (int j = 0; j < image1.cols; j++)
		{
			Vec3b bgrPixel = image1.at<Vec3b>(i, j);



			int tam = 1e8;
			for (int k = 0; k < mau.size(); k++)
			{
				int gt = abs((int)get <0>(mau[k]) - bgrPixel[0]) + abs((int)get <1>(mau[k]) - bgrPixel[1]) + abs((int)get <2>(mau[k]) - bgrPixel[2]);
				tam = min(tam, gt);
			}


			for (int k = 0; k < mau.size(); k++)
			{
				int gt = abs((int)get <0>(mau[k]) - bgrPixel[0]) + abs((int)get <1>(mau[k]) - bgrPixel[1]) + abs((int)get <2>(mau[k]) - bgrPixel[2]);
				if (gt == tam)
				{
					image1.at<Vec3b>(i, j) = { (unsigned char)get <0>(mau[k]), (unsigned char)get <1>(mau[k]), (unsigned char)get <2>(mau[k]) };
					break;
				}
			}
			
		}
	}

}
void xuLyAllAnhDatabase()
{

	
	ifstream ifs;
	ofstream ofs;

	ifs.open("E:\\temp\\bangPhoiMau\\images\\input_id.csv");  //tham so : id
	ofs.open("E:\\temp\\bangPhoiMau\\images\\output_database_color_board_id.csv"); // tra ve stt pallete

	string ss;
	Mat image1;
	//for(int ISS = 0; ISS < 50; ISS++)
	while(ifs >> ss)
	{
		
		//ifs >> ss;
		 
		int nm;

		nm = mau.size();

		ob c[45];



		for (int i = 0; i < 40; i++)
		{
			c[i].ID = i;
			c[i].x = 0;
			

		}

		map < tuple< unsigned char, unsigned char, unsigned char >, long long > mpix;


		for (char ID = '1'; ID <= '9'; ID++)
		{
			
			//"E:\temp\bangPhoiMau\images\database_image\a295304_1.png"
			string s = "E:\\temp\\bangPhoiMau\\images\\database_image\\a";
			
			s += ss;
			s += "_";
			s += ID;
			s += ".png";
			
			image1 = imread(s, IMREAD_COLOR);
			if (image1.empty()) 
				break;
			resize(image1, image1, { 500, 500 }, 0, 0, cv::INTER_NEAREST);

			xuLyMotAnh(image1);

			//cout << "ahah" << nm << '\n';
			

			for (int i = 0; i < image1.rows; i++)
			{
				for (int j = 0; j < image1.cols; j++)
				{
					Vec3b bgrPixel = image1.at<Vec3b>(i, j);

					mpix[{bgrPixel[0], bgrPixel[1], bgrPixel[2]}]++;
						

				}
			}
			

		}



		for (int I = 0; I < 40; I++)
		{
			for (int j = 0; j < bangMau[I].size(); j++)
			{
				tuple< unsigned char, unsigned char, unsigned char > tam = bangMau[I][j];
					c[I].x += mpix[tam];
				
			}
		}


		sort(c, c + 40, dk2);


		//FoCoBo[c[0].ID].push_back(ss);
		ofs << c[0].ID << '\n';

		
	}


	ifs.close();
	ofs.close();
	
}
int xuLyAllAnhInput()
{
	

	string ss;
	Mat image1;
	
	int nm;




	nm = mau.size();

	ob c[45];



	for (int i = 0; i < 40; i++)
	{
		c[i].ID = i;
		c[i].x = 0;

	}



	map < tuple< unsigned char, unsigned char, unsigned char >, long long > mpix;

	for (char ID = '1'; ID <= '8'; ID++)
	{
		
		//"E:\temp\bangPhoiMau\images\jpg2png\input_1.png"
		string s = "E:\\temp\\bangPhoiMau\\images\\jpg2png\\input_";

		s += ID;
		s += ".png";

		image1 = imread(s, IMREAD_COLOR);
		resize(image1, image1, { 500, 500 }, 0, 0, cv::INTER_NEAREST);

		xuLyMotAnh(image1);



		for (int i = 0; i < image1.rows; i++)
		{
			for (int j = 0; j < image1.cols; j++)
			{
				Vec3b bgrPixel = image1.at<Vec3b>(i, j);

				mpix[{bgrPixel[0], bgrPixel[1], bgrPixel[2]}]++;

			}
		}


	}



	
	for (int I = 0; I < 40; I++)
	{
		for (int j = 0; j < bangMau[I].size(); j++)
		{
			tuple< unsigned char, unsigned char, unsigned char > tam = bangMau[I][j];
			c[I].x += mpix[tam];
		}
	}

	sort(c, c + 40, dk2);

	int cid = c[0].ID;
	//cout << "bang mau: " << cid << '\n';
	 /*for(int i = 0; i < FoCoBo[cid].size(); i++)
		for (char j = '1'; j <= '3'; j++)
		{
			//"E:\temp\bangPhoiMau\images\a10334319_1.png"
			string s = "E:\\temp\\bangPhoiMau\\images\\a";

			s += FoCoBo[cid][i];
			s += "_";
			s += j;
			s += ".png";
			//cout << s << '\n';
			Mat image2 = imread(s, IMREAD_COLOR);

			resize(image2, image2, { 500, 500 }, 0, 0, cv::INTER_NEAREST);

			imshow("Image", image2);
			waitKey(0);
		}*/
	
	return c[0].ID;

	/*for (int I = 0; I < 7; I++)
	{
		cout << c[I].x << '\n';
	}*/

	


	
}
int main()
{
	
	// thuws tuwj 0 1 2 cuar Vec3b cos gioongs trong tuple khoong vaayj

	taoBangPhoiMau();
	xuLyAllAnhDatabase();
	xuLyAllAnhInput();
	//cout << "haha";

	return 0;
}

/*int fsh()
{

	// thuws tuwj 0 1 2 cuar Vec3b cos gioongs trong tuple khoong vaayj

	taoBangPhoiMau();
	xuLyAllAnhDatabase();
	return xuLyAllAnhInput();
	//cout << "haha";

	
}*/


