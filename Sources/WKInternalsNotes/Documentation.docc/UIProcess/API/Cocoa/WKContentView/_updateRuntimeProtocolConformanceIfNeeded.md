# ``WKInternalsNotes/WKContentView/_updateRuntimeProtocolConformanceIfNeeded()``

必要なプロトコル適合をランタイムで追加する。

## Objective-C Declaration
```objective-c
- (void)_updateRuntimeProtocolConformanceIfNeeded;
```

## Discussion
初回のみ実行される。BrowserEngineKit の使用状況に応じて `BETextInput` もしくは legacy UIKit プロトコル群を `class_addProtocol` で追加し、必要ならコンテキストメニューの async configuration 実装を差し替える。

## References
- [`WKContentViewInteraction.h#L914`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L914)
- [`WKContentViewInteraction.mm#L1254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1254)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
