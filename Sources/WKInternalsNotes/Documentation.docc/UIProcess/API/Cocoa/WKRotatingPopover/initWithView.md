# ``WKInternalsNotes/WKRotatingPopover/initWithView(_:)``

ビューと回転通知を設定する初期化子。

## Objective-C Declaration
```objective-c
- (id)initWithView:(WKContentView *)view;
```

## Discussion
`_view` を保持し、`presentationPoint` を `CGPointZero` に初期化する。`UIWindowWillRotateNotification` と `UIWindowDidRotateNotification` を監視する。

## References
- [`WKFormPopover.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.h#L35)
- [`WKFormPopover.mm#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPopover.mm#L87)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
