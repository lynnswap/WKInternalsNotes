# ``WKInternalsNotes/_WKDownload/originatingWebView``

ダウンロード元の `WKWebView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, weak) WKWebView *originatingWebView;
```

## Default Value
originating page が存在しない場合は `nil` を返す。

## Discussion
`DownloadProxy::originatingPage` を取得し、存在する場合は `WebPageProxy::cocoaView()` を返す。

## References
- [`_WKDownload.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L42)
- [`_WKDownload.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L90)
- [`_WKDownload.mm#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L92)
- [`_WKDownload.mm#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L93)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
