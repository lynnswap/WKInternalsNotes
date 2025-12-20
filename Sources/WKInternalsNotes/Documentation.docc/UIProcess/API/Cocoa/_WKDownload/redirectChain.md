# ``WKInternalsNotes/_WKDownload/redirectChain``

リダイレクトされた URL の配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSURL *> *redirectChain WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
リダイレクトがない場合は空配列になる。

## Discussion
`DownloadProxy::redirectChain` の要素を `NSURL` に変換し、`NSArray` として返す。

## References
- [`_WKDownload.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L43)
- [`_WKDownload.mm#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L96)
- [`_WKDownload.mm#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L98)
- [`_WKDownload.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
