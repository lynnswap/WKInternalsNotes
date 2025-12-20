# ``WKInternalsNotes/_WKNowPlayingMetadata/sourceApplicationIdentifier``

Now Playing を提供したアプリ識別子を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *sourceApplicationIdentifier;
```

## Default Value
生成直後は `nil`。`_setNowPlayingMetadataObserver` が発火すると `metadata.sourceApplicationIdentifier` をコピーして設定する。

## Discussion
テスト用の Now Playing メタデータ観測で `WebCore::NowPlayingMetadata` の `sourceApplicationIdentifier` を `NSString` に変換し、`setSourceApplicationIdentifier:` で代入して observer に渡す。`copy` 属性のため渡された文字列をコピー保持する。

## References
- [`WKWebViewPrivateForTesting.h#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L238)
- [`WKWebViewTesting.mm#L294`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L294)
- [`WKWebViewTesting.mm#L299`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L299)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
