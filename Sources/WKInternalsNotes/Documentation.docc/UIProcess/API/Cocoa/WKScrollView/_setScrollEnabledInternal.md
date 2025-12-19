# ``WKInternalsNotes/WKScrollView/_setScrollEnabledInternal(_:)``

内部側のスクロール可否を設定する。

## Objective-C Declaration
```objective-c
- (void)_setScrollEnabledInternal:(BOOL)enabled;
```

## Discussion
内部フラグを更新し、クライアント設定との AND で最終的な `scrollEnabled` を決める。

## References
- [`WKScrollView.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L41)
- [`WKScrollView.mm#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L462)
- [`WKScrollView.mm#L468`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L468)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
