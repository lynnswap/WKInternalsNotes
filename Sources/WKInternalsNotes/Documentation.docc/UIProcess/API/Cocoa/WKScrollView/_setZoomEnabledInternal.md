# ``WKInternalsNotes/WKScrollView/_setZoomEnabledInternal(_:)``

内部側のズーム可否を設定する。

## Objective-C Declaration
```objective-c
- (void)_setZoomEnabledInternal:(BOOL)enabled;
```

## Discussion
内部フラグを更新し、クライアント設定との AND で最終的な `zoomEnabled` を決める。

## References
- [`WKScrollView.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L42)
- [`WKScrollView.mm#L498`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L498)
- [`WKScrollView.mm#L504`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L504)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
