# ``WKInternalsNotes/WKWebViewContentProvider/web_setContentProviderData(_:suggestedFilename:completionHandler:)``

コンテンツデータを渡し、必要なら UI を表示する。

## Objective-C Declaration
```objective-c
- (void)web_setContentProviderData:(NSData *)data suggestedFilename:(NSString *)filename completionHandler:(void (^)(void))completionHandler;
```

## Discussion
`WKUSDPreviewView` ではデータとファイル名を保存し、3D プレビュー表示の確認ダイアログを出す。許可時に QuickLook 用のアイテムとサムネイルビューを作成し、完了ハンドラを呼ぶ。

## References
- [`WKWebViewContentProvider.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProvider.h#L42)
- [`WKUSDPreviewView.mm#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUSDPreviewView.mm#L92)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
