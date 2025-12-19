# ``WKInternalsNotes/WKContentView/_requestDOMPasteAccessForCategory(_:requiresInteraction:elementRect:originIdentifier:completionHandler:)``

DOM Paste のアクセス許可を要求する。

## Objective-C Declaration
```objective-c
- (void)_requestDOMPasteAccessForCategory:(WebCore::DOMPasteAccessCategory)pasteAccessCategory requiresInteraction:(WebCore::DOMPasteRequiresInteraction)requiresInteraction elementRect:(const WebCore::IntRect&)elementRect originIdentifier:(const String&)originIdentifier completionHandler:(CompletionHandler<void(WebCore::DOMPasteAccessResponse)>&&)completionHandler;
```

## Discussion
要求ハンドラを保存し、ユーザー操作不要で origin が一致する場合は即時許可する。そうでなければメニュー表示位置を算出して `UIMenuController` を提示する。

## References
- [`WKContentViewInteraction.h#L879`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L879)
- [`WKContentViewInteraction.mm#L8786`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8786)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
