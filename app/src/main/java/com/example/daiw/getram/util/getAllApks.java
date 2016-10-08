package com.example.daiw.getram.util;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by daiw on 2016/9/28.
 */
public class getAllApks extends Activity{

    //ways to get apk list installed
        public static List<PackageInfo> getAllApps(Context context){
        List<PackageInfo> apps = new ArrayList<PackageInfo>();
        PackageManager pm = context.getPackageManager();

        List<PackageInfo> packlist = pm.getInstalledPackages(0);
        for (int i=0;i<packlist.size();i++){
            PackageInfo pinfo = (PackageInfo)packlist.get(i);
            if ((pinfo.applicationInfo.flags & pinfo.applicationInfo.FLAG_SYSTEM) <= 0)
                apps.add(pinfo);
        }

        return apps;
        }


}
