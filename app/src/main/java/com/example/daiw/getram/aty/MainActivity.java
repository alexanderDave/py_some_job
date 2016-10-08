package com.example.daiw.getram.aty;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.content.pm.ResolveInfo;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.widget.AdapterView;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.GridView;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.daiw.getram.R;

import java.util.List;


public class MainActivity extends Activity {
    //private Button btn;
    GridView gridView;
    TextView tv;
    public List<ResolveInfo> apps;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_main);
        int i = loadapps();
        gridView = (GridView)findViewById(R.id.mian_gdview);
        tv = (TextView)findViewById(R.id.mian_text);
        gridView.setAdapter(new AppsAdapter());
        tv.setText("您共安装装" + apps.size() + "个应用文件其中非系统文件"+i);
        gridView.setOnItemClickListener(clickLinster);
    }

    private AdapterView.OnItemClickListener clickLinster = new AdapterView.OnItemClickListener() {
        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            ResolveInfo info = apps.get(position);
            String name = info.activityInfo.packageName;
            String cls = info.activityInfo.name;
            ComponentName com = new ComponentName(name,cls);

            Intent i = new Intent();
            i.setComponent(com);
            startActivity(i);
        }
    };

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    private int loadapps(){
        Intent intent  = new Intent(Intent.ACTION_MAIN,null);
        intent.addCategory(Intent.CATEGORY_LAUNCHER);
        new ImageView(MainActivity.this);
        int num = getPackageManager().queryIntentActivities(intent,0).size()-getPackageManager().queryIntentActivities(intent,-1).size();

        apps = getPackageManager().queryIntentActivities(intent,0);
        return num;
    }

    public class AppsAdapter extends BaseAdapter{
        public AppsAdapter(){

        }

        @Override
        public int getCount() {
            //Log.i("apps size",apps.size()+"");
            return apps.size();
        }

        @Override
        public Object getItem(int position) {
            return apps.get(position);
        }

        @Override
        public long getItemId(int position) {
            return position;
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            ImageView iv;

            if (null == convertView){
                iv = new ImageView(MainActivity.this);
                iv.setScaleType(ImageView.ScaleType.FIT_CENTER);
                iv.setLayoutParams(new GridView.LayoutParams(150,150));
            }else{
                iv = (ImageView) convertView;
            }
            ResolveInfo info = apps.get(position);
            iv.setImageDrawable(info.activityInfo.loadIcon(getPackageManager()));
            return iv;
        }
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
