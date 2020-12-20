package com.newbrank.controller;


import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.newbrank.mapper.ChannelMapper;
import com.newbrank.model.Channel;
import org.springframework.web.bind.annotation.GetMapping;
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
@RequestMapping("/channel")
@ResponseBody
public class ChannelController {

    @Resource
    ChannelMapper channelMapper;

    @GetMapping("/list")
    public List<Channel> getAll() {
        QueryWrapper<Channel> wrapper = new QueryWrapper<>();
        wrapper.select("name");
        return channelMapper.selectList(wrapper);
    }

}

