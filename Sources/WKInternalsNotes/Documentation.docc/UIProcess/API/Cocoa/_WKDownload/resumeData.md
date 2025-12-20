# ``WKInternalsNotes/_WKDownload/resumeData``

再開用の resume data を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *resumeData WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
内部の `DownloadProxy` が保持する resume data を返すため固定の既定値はない。

## Discussion
`DownloadProxy::legacyResumeData` を `NSData` としてラップして返す。

## References
- [`_WKDownload.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L45)
- [`_WKDownload.mm#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L108)
- [`_WKDownload.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
