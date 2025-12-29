# ``WKInternalsNotes/WKTextFinderClient/getImageForMatchResult(_:completionHandler:)``

検索結果の画像取得を開始する。

## Objective-C Declaration
```objective-c
- (void)getImageForMatchResult:(id <NSTextFinderAsynchronousDocumentFindMatch>)findMatch completionHandler:(void (^)(NSImage *generatedImage))completionHandler;
```

## Discussion
`_usePlatformFindUI` が無効なら `completionHandler(nil)` を即時実行する。`WKTextFinderMatch` を前提にコールバックをキューへ追加し、`getImageForFindMatch` を呼ぶ。

## References
- [`WKTextFinderClient.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.mm#L56)
- [`WKTextFinderClient.mm#L327`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.mm#L327)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
