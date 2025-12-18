# ``WKInternalsNotes/WKNavigationResponse/_navigation``

対応する WKNavigation を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKNavigation *_navigation WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Default Value
`_navigationResponse->navigation()` をラップした `WKNavigation`。

## Discussion
API::NavigationResponse が持つ navigation を Objective-C ラッパーとして返す。

## References
- [`WKNavigationResponsePrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponsePrivate.h#L33)
- [`WKNavigationResponse.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponse.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
