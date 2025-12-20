# ``WKInternalsNotes/WKKeyboardScrollViewAnimatorDelegate/keyboardScrollViewAnimator(_:distanceForIncrement:inDirection:)``

スクロール量を計算する。

## Objective-C Declaration
```objective-c
- (CGFloat)keyboardScrollViewAnimator:(WKKeyboardScrollViewAnimator *)animator distanceForIncrement:(WebCore::ScrollGranularity)increment inDirection:(WebCore::ScrollDirection)direction;
```

## Discussion
`WKContentView` では、`Document` は content view の bounds を webView 座標に変換したサイズ、`Page` は `Scrollbar::pageStep` を使ったサイズ、`Line` は `Scrollbar::pixelsPerLineStep()` を webView 座標に変換した高さを返す。`Pixel` は 0 を返す。

## References
- [`WKKeyboardScrollingAnimator.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKKeyboardScrollingAnimator.h#L63)
- [`WKContentViewInteraction.mm#L7854`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7854)
- [`WKContentViewInteraction.mm#L7859`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7859)
- [`WKContentViewInteraction.mm#L7864`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7864)
- [`WKContentViewInteraction.mm#L7867`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7867)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
