# ``WKInternalsNotes/WKContentView/_showShareSheet(_:inRect:completionHandler:)``

共有シートを表示する。

## Objective-C Declaration
```objective-c
- (void)_showShareSheet:(const WebCore::ShareDataWithParsedURL&)shareData inRect:(std::optional<WebCore::FloatRect>)rect completionHandler:(WTF::CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
共有シートが既に表示中なら `ResetState` で閉じる。`WKShareSheet` を生成して delegate を設定し、`rect` が無い場合はマウス位置から表示矩形を補完した上で `presentWithParameters:inRect:completionHandler:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L830`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L830)
- [`WKContentViewInteraction.mm#L9721`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9721)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
