package com.example.daiw.getram.aty;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.Window;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

import com.example.daiw.getram.R;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by daiw on 2016/9/28.
 */
public class DemoActivity extends Activity{

    private ListView mlistView = null;
    private TextView mtext = null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_demo);
        //find list content
        mtext = (TextView)findViewById(R.id.demo_txtview);
        mlistView = (ListView)findViewById(R.id.demo_listapp);

        List<PackageInfo> apps = new ArrayList<PackageInfo>();
        PackageManager pm = this.getPackageManager();
        List<PackageInfo> packageInfos = pm.getInstalledPackages(0);
        for (int i = 0;i<packageInfos.size();i++){
            PackageInfo pinfo = (PackageInfo)packageInfos.get(i);
            if ((pinfo.applicationInfo.flags & pinfo.applicationInfo.FLAG_SYSTEM) > 0)
                apps.add(pinfo);
        }

        mtext.setText("all apks list here:"+apps.size());
        mlistView.setAdapter(new ArrayAdapter(this,android.R.layout.simple_list_item_1,apps));
    }




    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
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
