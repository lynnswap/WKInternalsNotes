# ``WKInternalsNotes/WKBaseScrollView/baseScrollViewDelegate``

WKBaseScrollView の delegate を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id<WKBaseScrollViewDelegate> baseScrollViewDelegate;
```

## Default Value
未設定の場合は `nil`。

## Discussion
`axesToPreventScrollingForPanGestureInScrollView:` でスクロール抑止軸を取得し、`shouldAllowPanGestureRecognizerToReceiveTouchesInScrollView:` でタッチ受け取り可否を判定する。

## References
- [`WKBaseScrollView.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L55)
- [`WKBaseScrollView.mm#L236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L236)
- [`WKBaseScrollView.mm#L299`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L299)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
