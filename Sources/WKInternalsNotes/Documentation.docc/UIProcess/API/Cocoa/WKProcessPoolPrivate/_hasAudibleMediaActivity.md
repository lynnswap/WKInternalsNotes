# ``WKInternalsNotes/WKProcessPool/_hasAudibleMediaActivity()``

可聴メディア再生があるかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_hasAudibleMediaActivity WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`_processPool->hasAudibleMediaActivity()` の結果を YES/NO に変換して返す。

## References
- [`WKProcessPoolPrivate.h#L153`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L153)
- [`WKProcessPool.mm#L433`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L433)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
