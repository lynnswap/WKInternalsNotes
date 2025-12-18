# ``WKInternalsNotes/WKNavigationAction/_clickLocationInRootViewCoordinates``

クリック位置をルートビュー座標で返す（iOS のみ）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGPoint _clickLocationInRootViewCoordinates WK_API_AVAILABLE(ios(11.0));
```

## Default Value
`_navigationAction->clickLocationInRootViewCoordinates()` の結果。

## Discussion
`PLATFORM(IOS_FAMILY)` の場合のみ実装され、クリック位置の座標を `CGPoint` として返す。

## References
- [`WKNavigationActionPrivate.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L58)
- [`WKNavigationAction.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L139)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
