# ``WKInternalsNotes/WKNavigationResponse/_navigationInitiatingFrame``

ナビゲーション開始フレームの情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKFrameInfo *_navigationInitiatingFrame WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Default Value
`_navigationResponse->navigationInitiatingFrame()` をラップした `WKFrameInfo`。

## Discussion
navigation initiating frame が存在する場合に `WKFrameInfo` として返す。

## References
- [`WKNavigationResponsePrivate.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponsePrivate.h#L32)
- [`WKNavigationResponse.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponse.mm#L84)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
