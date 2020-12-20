package com.newbrank.controller;


import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.newbrank.mapper.VideosMapper;
import com.newbrank.model.Videos;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;

/**
 * <p>
 * 前端控制器
 * </p>
 *
 * @author christopher
 * @since 2020-11-19
 */
@Controller
@RequestMapping("/videos")
@ResponseBody
public class VideosController {

    @Resource
    VideosMapper videosMapper;

    @GetMapping("/up/{uid}/size/{size}/page/{pageNum}")
    public IPage<Videos> getVideoByUidAndPageNum(@PathVariable String uid,
                                                 @PathVariable int pageNum,
                                                 @PathVariable int size) {
        QueryWrapper<Videos> wrapper = new QueryWrapper<>();
        wrapper.eq("uid", uid);
        return videosMapper.selectPage(new Page<Videos>(pageNum, size), wrapper);
    }

}

