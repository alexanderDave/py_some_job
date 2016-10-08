package com.example.daiw.getram.adapter;

import android.content.pm.ResolveInfo;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;

import com.example.daiw.getram.aty.LauncherAty;
import com.example.daiw.getram.aty.MainActivity;

import java.util.List;

/**
 * Created by daiw on 2016/10/8.
 */
public class Adpter4gdview extends BaseAdapter {
    private List<ResolveInfo> apps;

    public Adpter4gdview(List apps){
        this.apps = apps;
    }

    @Override
    public int getCount() {
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
        if (convertView == null){

        }
        return null;
    }
}
