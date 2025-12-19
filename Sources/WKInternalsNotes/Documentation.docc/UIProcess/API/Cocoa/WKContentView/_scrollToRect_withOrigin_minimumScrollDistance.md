# ``WKInternalsNotes/WKContentView/_scrollToRect(_:withOrigin:minimumScrollDistance:)``

指定矩形へのスクロールを要求する。

## Objective-C Declaration
```objective-c
- (BOOL)_scrollToRect:(CGRect)targetRect withOrigin:(CGPoint)origin minimumScrollDistance:(CGFloat)minimumScrollDistance;
```

## Discussion
`WKWebView` の `_scrollToRect:origin:minimumScrollDistance:` に処理を委譲する。

## References
- [`WKContentView.h#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L133)
- [`WKContentView.mm#L1051`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1051)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
