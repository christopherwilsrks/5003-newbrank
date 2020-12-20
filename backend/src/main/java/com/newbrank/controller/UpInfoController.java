package com.newbrank.controller;


import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.newbrank.mapper.UpInfoMapper;
import com.newbrank.model.UpInfo;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import java.util.List;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author christopher
 * @since 2020-11-19
 */
@Controller
@RequestMapping("/up")
@ResponseBody
public class UpInfoController {

    @Resource
    UpInfoMapper upInfoMapper;

    @GetMapping("/list/{channel}")
    public List<UpInfo> getListByChannel(@PathVariable String channel) {
        QueryWrapper<UpInfo> wrapper = new QueryWrapper<>();
        wrapper.eq("channel", channel);
        return upInfoMapper.selectList(wrapper);
    }

    @GetMapping("/{uid}")
    public UpInfo getUpByUid(@PathVariable String uid) {
        QueryWrapper<UpInfo> wrapper = new QueryWrapper<>();
        wrapper.eq("uid", uid);
        return upInfoMapper.selectOne(wrapper);
    }

}

