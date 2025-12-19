# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:saveDataToFile:suggestedFilename:mimeType:originatingURL:)``

ダウンロードデータの保存処理を delegate に委譲する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView saveDataToFile:(NSData *)data suggestedFilename:(NSString *)suggestedFilename mimeType:(NSString *)mimeType originatingURL:(NSURL *)url WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIDelegate::UIClient の `saveDataToFileInDownloadsFolder` がデータ本体とファイル名、MIME type、元 URL を渡して保存を依頼する。

## References
- [`WKUIDelegatePrivate.h#L301`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L301)
- [`UIDelegate.mm#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L145)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
