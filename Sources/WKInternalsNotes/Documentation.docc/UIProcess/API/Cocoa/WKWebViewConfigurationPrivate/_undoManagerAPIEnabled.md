# ``WKInternalsNotes/WKWebViewConfiguration/_undoManagerAPIEnabled``

UndoManager API を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUndoManagerAPIEnabled:) BOOL _undoManagerAPIEnabled WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_undoManagerAPIEnabled = YES`: UndoManager API を有効化。
- `_undoManagerAPIEnabled = NO`: UndoManager API を有効化（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L148)
- [`WKWebViewConfiguration.mm#L1438`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1438)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
