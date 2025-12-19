# ``WKInternalsNotes/WKNavigationAction/_syntheticClickType``

合成クリック種別を返す（iOS のみ）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKSyntheticClickType _syntheticClickType WK_API_AVAILABLE(ios(10.0));
```

## Default Value
`toWKSyntheticClickType(_navigationAction->syntheticClickType())` の結果。

## Discussion
`PLATFORM(IOS_FAMILY)` の場合のみ実装され、`syntheticClickType()` を `WKSyntheticClickType` に変換して返す。

## References
- [`WKNavigationActionPrivate.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L57)
- [`WKNavigationAction.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
