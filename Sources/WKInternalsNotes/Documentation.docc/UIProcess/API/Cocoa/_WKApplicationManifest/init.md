# ``WKInternalsNotes/_WKApplicationManifest/init()``

利用できない初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
`_WKApplicationManifest` は JSON からの初期化専用で、`initWithJSONData:manifestURL:documentURL:` を使用する。

## References
- [`_WKApplicationManifest.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L72)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
