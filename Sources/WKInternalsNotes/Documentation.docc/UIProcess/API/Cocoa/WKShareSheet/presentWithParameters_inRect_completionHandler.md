# ``WKInternalsNotes/WKShareSheet/presentWithParameters(_:inRect:completionHandler:)``

共有シートを表示する。

## Objective-C Declaration
```objective-c
- (void)presentWithParameters:(const WebCore::ShareDataWithParsedURL&)data inRect:(std::optional<WebCore::FloatRect>)rect completionHandler:(WTF::CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
共有データを配列化し、必要なら一時ディレクトリへファイルを書き出した上で共有 UI を提示する。完了時には `completionHandler` を呼び出す。

## References
- [`WKShareSheet.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.h#L45)
- [`WKShareSheet.mm#L309`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.mm#L309)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
