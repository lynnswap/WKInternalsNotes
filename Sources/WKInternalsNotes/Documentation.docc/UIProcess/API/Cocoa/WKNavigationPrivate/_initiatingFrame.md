# ``WKInternalsNotes/WKNavigation/_initiatingFrame``

ナビゲーションを開始したフレーム情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) WKFrameInfo *_initiatingFrame WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Default Value
`_navigation->originatingFrameInfo()` から生成した `WKFrameInfo`。

## Discussion
`originatingFrameInfo()` が null の場合は `nil` を返す。存在する場合は `frameID` から `WebFrameProxy` を取得し、`FrameInfoData` を作って `API::FrameInfo::create` をラップして返す。

## References
- [`WKNavigationPrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationPrivate.h#L33)
- [`WKNavigation.mm#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigation.mm#L63)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
