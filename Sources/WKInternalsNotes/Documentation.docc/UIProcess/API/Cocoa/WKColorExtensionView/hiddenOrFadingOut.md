# ``WKInternalsNotes/WKColorExtensionView/hiddenOrFadingOut``

非表示またはフェードアウト中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isHiddenOrFadingOut) BOOL hiddenOrFadingOut;
```

## Discussion
`hidden` が `YES` もしくは内部の `_isVisible` が `NO` の場合に `YES` を返す。

## References
- [`WKColorExtensionView.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.h#L51)
- [`WKColorExtensionView.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L111)
- [`WKColorExtensionView.mm#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L113)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
