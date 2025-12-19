# ``WKInternalsNotes/WKWebView/_proofreadingSessionUpdateState(_:forSuggestionWithUUID:)``

`_proofreadingSessionUpdateState` を実行する。

## Objective-C Declaration
```objective-c
- (void)_proofreadingSessionUpdateState:(WebCore::WritingTools::TextSuggestionState)state forSuggestionWithUUID:(NSUUID *)replacementUUID;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L539`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L539)
- [`WKWebView.mm#L2879`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2879)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
