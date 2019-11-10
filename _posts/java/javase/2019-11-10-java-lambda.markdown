---
layout: post
title: 'java中最强语法--lambda表达式'
date: 2019-11-10
tags: Java basis
---


<div class="article-entry" itemprop="articleBody" lg-uid="lg0">
            <h3 id="lambda表达式"><a href="#lambda表达式" class="headerlink" title="lambda表达式"></a>lambda表达式</h3><p>lambda表达式形式：参数，箭头(-&gt;)以及一个表达式，也可以将操作放在代码块{}中。</p>
<figure class="highlight java"><table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br></pre></td><td class="code"><pre><span class="line">(String first,String second)-&gt;</span><br><span class="line">{</span><br><span class="line">	<span class="keyword">if</span>(first.length()&gt;second.length()) <span class="keyword">return</span> <span class="number">1</span>;</span><br><span class="line">	<span class="keyword">else</span> <span class="keyword">if</span>(first.length()&lt;second.length()) <span class="keyword">return</span> -<span class="number">1</span>;</span><br><span class="line">	<span class="keyword">else</span> <span class="keyword">return</span> <span class="number">0</span>;</span><br><span class="line">}</span><br><span class="line"></span><br><span class="line">() -&gt; System.out.pringln(<span class="string">"i"</span>);</span><br></pre></td></tr></tbody></table></figure>

<p>对于只有一个抽象方法的接口，需要这种接口的对象时，就可以提供一个lambda表达式。这种接口称为函数式接口。Comparator 就是只有一个方法的接口， 所以可以提供一个lambda 表达式：</p>
<p>函数式接口中可以包含静态方法（已经实现了的方法），默认方法（default），java.lang.Object里的public方法。</p>
<figure class="highlight java"><table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br></pre></td><td class="code"><pre><span class="line">Arrays.sort (words ,</span><br><span class="line">	(first , second) -&gt; first.length() - second.length()) ;</span><br></pre></td></tr></tbody></table></figure>

<h3 id="方法引用"><a href="#方法引用" class="headerlink" title="方法引用"></a>方法引用</h3><figure class="highlight java"><table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br></pre></td><td class="code"><pre><span class="line">Timer t = <span class="keyword">new</span> Timer(<span class="number">1000</span>, event -&gt; System.out.println(event))；</span><br><span class="line"><span class="comment">//等价于</span></span><br><span class="line">Timer t = <span class="keyword">new</span> Timer(<span class="number">1000</span>, System.out::println);</span><br></pre></td></tr></tbody></table></figure>

<p>表达式System.out::println是一个方法引用，等价于前面的lambda表达式。主要有3中形式：</p>
<figure class="highlight sas"><table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br></pre></td><td class="code"><pre><span class="line">//System.<span class="meta">out</span>.println == <span class="meta">x</span>-&gt;System.<span class="meta">out</span>.print<span class="meta">ln(</span><span class="meta">x</span>)</span><br><span class="line">object::instanceMethod</span><br><span class="line">//Math.pow(<span class="meta">x</span>,y) == (<span class="meta">x</span>,y)-&gt;Math.pow(<span class="meta">x</span>,y)</span><br><span class="line">Class::staticMethod</span><br><span class="line">//String::compareToIgnoreCase == (<span class="meta">x</span>,y)-&gt;<span class="meta">x</span>.compareToIgnoreCase(y)</span><br><span class="line">Class::instanceMethod</span><br></pre></td></tr></tbody></table></figure>


        </div>