# ``WKInternalsNotes/_WKDownload/request``

ダウンロード開始時のリクエストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURLRequest *request;
```

## Default Value
内部の `DownloadProxy` が保持する request を返すため固定の既定値はない。

## Discussion
`DownloadProxy::request` を `HTTPBodyUpdatePolicy::DoNotUpdateHTTPBody` で `NSURLRequest` に変換して返す。

## References
- [`_WKDownload.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L41)
- [`_WKDownload.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L85)
- [`_WKDownload.mm#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L87)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
